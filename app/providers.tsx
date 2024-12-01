'use client';

import { SWRConfig } from 'swr';

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SWRConfig 
      value={{
        refreshInterval: 60000,
        revalidateOnFocus: true,
        fetcher: async (url: string) => {
          const res = await fetch(url);
          if (!res.ok) {
            const error = await res.json();
            throw new Error(error.error || 'An error occurred while fetching the data.');
          }
          return res.json();
        }
      }}
    >
      {children}
    </SWRConfig>
  );
}