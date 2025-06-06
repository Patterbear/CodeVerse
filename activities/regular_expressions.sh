file="$1"

awk '
{
  for (i = 1; i < NF; i++) {
    if (tolower($i) == "thy") {
      nextWord = $(i+1)
      gsub(/[^a-zA-Z0-9]/, "", nextWord)
      counts[tolower(nextWord)]++
    }
}
}
END {
  for (word in counts) {
    print counts[word], word
  }
}
' "$file" | sort -nr