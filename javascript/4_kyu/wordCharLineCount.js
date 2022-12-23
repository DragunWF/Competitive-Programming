// https://www.codewars.com/kata/5286a298f8fc1b7667000c1c/train/javascript

function DocumentParser(reader) {
  this.reader = reader;
  let text = readText(this.reader);

  const lines = text.split("\n");
  this.charCount = lines.join("").length;
  this.lineCount = this.charCount > 0 ? lines.length : 0;

  this.wordCount = 0;
  if (this.charCount > 0) {
    for (let line of lines) {
      this.wordCount += line.split(" ").filter((x) => {
        return x !== "";
      }).length;
    }
  }
}

function readText(reader) {
  let output = "";
  while (true) {
    let chunk = reader.getChunk();
    if (chunk === "") break;
    output += chunk;
  }
  return output;
}

DocumentParser.prototype.parse = () => {};

function test() {
  function FileReaderSimulator(text) {
    let index = -1;
    this.getChunk = function () {
      index++;
      return index == text.length ? "" : text.charAt(index);
    };
  }

  const fileContent = `Once upon a time
There was a boy and a girl.
And they lived happily ever after.`,
    reader = new FileReaderSimulator(fileContent),
    parser = new DocumentParser(reader);
}

test();
