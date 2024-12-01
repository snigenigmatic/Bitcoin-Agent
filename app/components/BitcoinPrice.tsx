'use client';

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useBitcoinPrice } from "../hooks/useBitcoinPrice";
import { Bitcoin } from "lucide-react";

export function BitcoinPrice() {
  const { price, timestamp, isLoading, isError } = useBitcoinPrice();

  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">Bitcoin Price</CardTitle>
        <Bitcoin className="h-4 w-4 text-muted-foreground" />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">
          {isLoading ? (
            "Loading..."
          ) : isError ? (
            "Error loading price"
          ) : price ? (
            `$${price.toLocaleString()}`
          ) : (
            "No data available"
          )}
        </div>
        {timestamp && !isError && !isLoading && (
          <p className="text-xs text-muted-foreground">
            {timestamp}
          </p>
        )}
      </CardContent>
    </Card>
  );
}