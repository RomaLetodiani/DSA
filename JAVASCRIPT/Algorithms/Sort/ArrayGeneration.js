const generateArray = (size = 10000, min = -20000, max = 20000) => {
  return Array.from({ length: size }, () => Math.floor(Math.random() * (max - min + 1)) + min);
};

module.exports = generateArray;
