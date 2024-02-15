// https://www.codewars.com/kata/5351b35ebaeb67f9110012d2

function createSecretHolder(secret) {
  return {
    value: secret,
    setSecret: function (newValue) {
      this.value = newValue;
    },
    getSecret: function (newValue) {
      return this.value;
    },
  };
}

// test code
const secret = createSecretHolder(5);
console.log(secret.getSecret());
