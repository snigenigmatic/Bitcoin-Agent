'use client';

import useSWR from 'swr';

export interface BitcoinPriceData {
  usd: number;
  timestamp: string;
}

export function useBitcoinPrice() {
  const { data, error, isLoading } = useSWR<BitcoinPriceData>('/api/bitcoin');

  return {
    price: data?.usd,
    timestamp: data?.timestamp,
    isLoading,
    isError: error,
  };
}