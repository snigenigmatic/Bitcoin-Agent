import { NextResponse } from 'next/server';

export const dynamic = 'force-dynamic';

export async function POST(req: Request) {
  try {
    const { query, language } = await req.json();
    console.log('Received query:', { query, language }); // Debug log

    const response = await fetch('http://localhost:8000/api/query', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query, language }),
    });

    if (!response.ok) {
      console.error('Backend error:', response.status, await response.text()); // Debug log
      throw new Error(`Backend returned ${response.status}`);
    }

    const data = await response.json();
    console.log('Backend response:', data); // Debug log
    
    if (data.error) {
      throw new Error(data.error);
    }

    return NextResponse.json(data);
  } catch (error) {
    console.error('Query processing error:', error); // Debug log
    return NextResponse.json(
      { error: `Failed to process query: ${error.message}` },
      { status: 500 }
    );
  }
}