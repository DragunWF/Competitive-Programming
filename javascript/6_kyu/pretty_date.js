// https://www.codewars.com/kata/53988ee02c2414dbad000baa

function toPretty(s) {
  if (s < 1) return "just now";
  if (s < 60) return `${s > 1 ? `${s} seconds` : "a second"} ago`;
  if (s < 3600)
    return `${s > 120 ? `${Math.floor(s / 60)} minutes` : "a minute"} ago`;
  if (s < 86400)
    return `${s > 7200 ? `${Math.floor(s / 3600)} hours` : "an hour"} ago`;
  if (s < 604800)
    return `${s > 172800 ? `${Math.floor(s / 86400)} days` : "a day"} ago`;
  if (s >= 604800)
    return `${s > 1209600 ? `${Math.floor(s / 604800)} weeks` : "a week"} ago`;
}
