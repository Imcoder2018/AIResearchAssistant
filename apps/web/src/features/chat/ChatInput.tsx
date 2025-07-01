"use client";
import React, { useState } from "react";
import { Button } from "../../components/ui/Button";
import { useChatStore } from "../../stores/chatStore";
import { sendChatMessage } from "../../lib/api";

interface ChatInputProps {
  // No props needed since actions are from store
}

export const ChatInput: React.FC<ChatInputProps> = () => {
  const [input, setInput] = useState("");
  const { threadId, addMessage, toggleLoading } = useChatStore();

  const handleSend = async () => {
    if (input.trim()) {
      // Add user message to store
      addMessage({ role: "user", content: input });
      setInput("");
      toggleLoading(true);
      
      // Send message to API
      await sendChatMessage(input, threadId);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="p-4 border-t bg-white">
      <div className="relative">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your message..."
          className="w-full p-3 pr-12 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
          rows={3}
        />
        <Button
          onClick={handleSend}
          className="absolute bottom-3 right-3"
          size="sm"
        >
          Send
        </Button>
      </div>
    </div>
  );
};
