import { create } from "zustand";

interface Message {
  role: string;
  content: string;
}

interface ChatState {
  messages: Message[];
  threadId: string | null;
  isLoading: boolean;
  addMessage: (message: Message) => void;
  updateLastMessageContent: (content: string) => void;
  setThreadId: (threadId: string) => void;
  toggleLoading: (state: boolean) => void;
  clearChat: () => void;
}

export const useChatStore = create<ChatState>((set) => ({
  messages: [],
  threadId: null,
  isLoading: false,
  
  addMessage: (message) => set((state) => ({ messages: [...state.messages, message] })),
  
  updateLastMessageContent: (content) => 
    set((state) => {
      if (state.messages.length === 0) return state;
      const updatedMessages = [...state.messages];
      updatedMessages[updatedMessages.length - 1].content = content;
      return { messages: updatedMessages };
    }),
  
  setThreadId: (threadId) => set({ threadId }),
  
  toggleLoading: (state) => set({ isLoading: state }),
  
  clearChat: () => set({ messages: [], threadId: null }),
}));
