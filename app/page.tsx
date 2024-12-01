import { QueryForm } from './components/QueryForm';

export default function Home() {
  return (
    <main className="min-h-screen bg-background p-8">
      <div className="mx-auto max-w-7xl space-y-8">
        <h1 className="text-4xl font-bold">AI Workflow Dashboard</h1>
        
        <div className="max-w-2xl mx-auto">
          <QueryForm />
        </div>
      </div>
    </main>
  );
}