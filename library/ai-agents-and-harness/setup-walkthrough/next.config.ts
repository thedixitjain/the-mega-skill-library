import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // The chat page calls /api/session once on mount to create (or resume) the
  // Managed Agents session. React strict mode double-runs effects in dev, which would
  // race two session creates, so the effect guards itself with a ref instead
  // of relying on this flag. Nothing here is load-bearing.
  reactStrictMode: true,
};

export default nextConfig;
