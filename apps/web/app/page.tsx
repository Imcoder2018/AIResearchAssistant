import { ChatWindow } from "../src/features/chat/ChatWindow";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4">
      <h1 className="text-2xl font-semibold mb-4">AI Research Assistant</h1>
      <ChatWindow />
    </main>
  );
}
