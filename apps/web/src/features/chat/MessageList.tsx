"use client";
import React, { useEffect, useRef } from "react";
import { useChatStore } from "../../stores/chatStore";

interface Message {
  role: string;
  content: string;
}

interface MessageListProps {
  // No props needed since messages are from store
}

export const MessageList: React.FC<MessageListProps> = () => {
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const messages = useChatStore((state) => state.messages);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages]);

  return (
    <div className="flex-1 p-4 overflow-y-auto bg-gray-50">
      {messages.length === 0 ? (
        <div className="flex items-center justify-center h-full text-gray-500">
          Start a conversation with the AI Research Assistant
        </div>
      ) : (
        messages.map((message, index) => (
          <div
            key={index}
            className={`mb-4 ${message.role === "user" ? "text-right" : "text-left"}`}
          >
            <div
              className={`inline-block p-3 rounded-lg max-w-[80%] ${
                message.role === "user"
                  ? "bg-blue-500 text-white"
                  : "bg-white text-gray-800 shadow-sm"
              }`}
            >
              <span className="font-medium">{message.role === "user" ? "You" : "Assistant"}</span>
              <div className="mt-1">{message.content}</div>
            </div>
          </div>
        ))
      )}
      <div ref={messagesEndRef} />
    </div>
  );
};
