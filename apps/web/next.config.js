/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'https://ainextfastapibackend-f73o9zd42-imcoder2018s-projects.vercel.app/v1/:path*',
      },
    ];
  },
};

module.exports = nextConfig;
