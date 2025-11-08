#!/bin/bash
# Build the Jekyll site for production

echo "Building Jekyll site..."
bundle exec jekyll build

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Build successful!"
    echo "Site generated in: _site/"
else
    echo ""
    echo "✗ Build failed!"
    exit 1
fi
