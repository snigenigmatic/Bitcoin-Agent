import { NextResponse } from 'next/server';

export const dynamic = 'force-dynamic';

export async function GET() {
  try {
    const response = await fetch('http://localhost:8000/api/bitcoin');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    if (data.error) {
      throw new Error(data.error);
    }
    return NextResponse.json(data);
  } catch (error) {
    console.error('Bitcoin API error:', error);
    return NextResponse.json(
      { error: 'Failed to fetch Bitcoin price' }, 
      { status: 500 }
    );
  }
}