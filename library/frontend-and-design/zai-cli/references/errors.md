# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Z_AI_API_KEY not set | Environment variable missing | Export the key: `export Z_AI_API_KEY="your-api-key"` |
| Invalid API key | Key revoked or incorrect | Verify key at https://z.ai/manage-apikey/apikey-list |
| Rate limit exceeded | Too many requests | Wait and retry, or upgrade API tier |
| Network timeout | Connectivity issues or slow response | Check internet connection, retry with longer timeout |
| File not found | Invalid path to image/video | Verify file path exists and is accessible |
| Unsupported format | Image/video format not supported | Convert to supported format (PNG, JPG, MP4) |
| Repository not found | Invalid GitHub repo path | Verify repository exists and is public (or authenticated) |
| Empty search results | No matches for query | Broaden search terms or check spelling |

---
*[Tons of Skills](https://tonsofskills.com) by [Intent Solutions](https://intentsolutions.io) | [jeremylongshore.com](https://jeremylongshore.com)*
