import { useChatStore } from "../stores/chatStore";

/**
 * Send a chat message to the FastAPI backend and handle streaming response.
 * @param message The user's message content
 * @param threadId The thread ID for continuing a conversation, or null for a new one
 * @returns Promise resolving when the stream is complete
 */
export async function sendChatMessage(message: string, threadId: string | null): Promise<void> {
  const store = useChatStore.getState();
  store.toggleLoading(true);
  store.addMessage({ role: "user", content: message });

  try {
    const baseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
    const response = await fetch(`${baseUrl}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message,
        thread_id: threadId,
      }),
    });

    if (!response.ok) {
      throw new Error(`API request failed with status ${response.status}`);
    }

    if (!response.body) {
      throw new Error('Response body is null');
    }

    // Add an initial empty assistant message that we'll update with streaming content
    store.addMessage({ role: "assistant", content: "" });

    const reader = response.body.getReader();
    const decoder = new TextDecoder('utf-8');
    let done = false;

    while (!done) {
      const { value, done: readerDone } = await reader.read();
      done = readerDone;

      if (value) {
        const chunk = decoder.decode(value, { stream: true });
        try {
          const parsed = JSON.parse(chunk);
          if (parsed.content) {
            store.updateLastMessageContent(parsed.content);
          }
          if (parsed.thread_id && parsed.thread_id !== threadId) {
            store.setThreadId(parsed.thread_id);
          }
        } catch (e) {
          console.error('Error parsing JSON from stream chunk:', e, chunk);
        }
      }
    }
  } catch (error) {
    console.error('Error sending chat message:', error);
    store.updateLastMessageContent(`Error: Unable to get response from server. ${error instanceof Error ? error.message : ''}`);
  } finally {
    store.toggleLoading(false);
  }
}
