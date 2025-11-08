#!/bin/bash
# Start Jekyll development server with live reload

echo "Starting Jekyll with live reload..."
echo "Server will be available at: http://127.0.0.1:4000/CLRS/"
echo ""
echo "Features:"
echo "  - Auto-regeneration: Files are rebuilt automatically on save"
echo "  - LiveReload: Browser refreshes automatically on changes"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

bundle exec jekyll serve --livereload
