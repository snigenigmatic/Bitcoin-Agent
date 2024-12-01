export async function submitQuery(query: string, language: string) {
  const response = await fetch('/api/query', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query, language }),
  });
  
  if (!response.ok) {
    throw new Error('Failed to process query');
  }
  
  return response.json();
}