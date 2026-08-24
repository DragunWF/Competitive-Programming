# https://leetcode.com/problems/encode-and-decode-tinyurl/description/

class Codec:
    start = "https"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url_parts = longUrl.split("://")
        Codec.start = url_parts[0]
        return url_parts[1]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return f"{Codec.start}://{shortUrl}"
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))