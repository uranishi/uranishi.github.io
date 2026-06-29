#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export PATH="/opt/homebrew/opt/ruby@3.3/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:/opt/homebrew/bin:${PATH}"

if [[ -d "$ROOT/.venv/bin" ]]; then
  export PATH="$ROOT/.venv/bin:$PATH"
fi

if ! command -v ruby >/dev/null || ! ruby -e 'exit(Gem::Version.new(RUBY_VERSION) >= Gem::Version.new("3.0") ? 0 : 1)'; then
  echo "Ruby 3.0+ is required. Install with: brew install ruby@3.3" >&2
  exit 1
fi

if ! command -v convert >/dev/null; then
  echo "ImageMagick is required. Install with: brew install imagemagick" >&2
  exit 1
fi

if [[ ! -d vendor/bundle ]] && [[ ! -f Gemfile.lock ]]; then
  bundle install
fi

if [[ ! -x "$ROOT/.venv/bin/jupyter" ]]; then
  python3 -m venv "$ROOT/.venv"
  "$ROOT/.venv/bin/pip" install nbconvert jupyter
fi

PORT="${1:-4000}"
echo "Generating papers.bib from _data/publications.json..."
python3 "$ROOT/bin/export_publications.py"

echo "Starting Jekyll at http://127.0.0.1:${PORT}/"
bundle exec jekyll serve --livereload --port="$PORT" --host=127.0.0.1
