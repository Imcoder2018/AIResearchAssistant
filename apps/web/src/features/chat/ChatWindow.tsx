"use client";
import React from "react";
import { useChatStore } from "../../stores/chatStore";
import { MessageList } from "./MessageList";
import { ChatInput } from "./ChatInput";

interface ChatWindowProps {
  // No props needed since state is managed by Zustand
}

export const ChatWindow: React.FC<ChatWindowProps> = () => {
  const { threadId, setThreadId } = useChatStore();
  
  // This would be updated with actual API integration in a later step
  const handleThreadIdChange = (newThreadId: string) => {
    setThreadId(newThreadId);
  };

  return (
    <div className="flex flex-col h-full bg-white rounded-lg shadow-md overflow-hidden">
      <div className="p-4 border-b">
        <h2 className="text-xl font-semibold text-gray-800">AI Research Assistant</h2>
        {threadId && <p className="text-sm text-gray-500">Thread ID: {threadId}</p>}
      </div>
      <MessageList />
      <ChatInput />
    </div>
  );
};
