# Image Optimization Guidelines

This directory contains all static images for the Docusaurus site. For optimal performance in production:

## Image Optimization

1. **Compress images** before adding them to the site
   - Use tools like TinyPNG, ImageOptim, or Squoosh
   - Keep file sizes minimal without sacrificing quality

2. **Use appropriate formats**
   - Use WebP format when possible for better compression
   - SVG for vector graphics and logos
   - JPEG for photos
   - PNG for graphics with transparency

3. **Choose proper dimensions**
   - Resize images to their largest intended display size
   - Avoid using large images and scaling them down with CSS

## Social Card

`docusaurus-social-card.jpg` is used for social media previews when sharing links. Ensure this image is:
- 1200x630 pixels (for Twitter)
- 1200x630 pixels (for LinkedIn)
- 800x418 pixels (for Facebook is acceptable)

## Favicon

The favicon.ico should be a multi-size icon file including 16x16, 32x32, and 48x48 pixel sizes.