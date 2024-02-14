export const generateArray = (size: number = 10000, min: number = -20000, max: number = 20000): number[] => {
  return Array.from({ length: size }, () => Math.floor(Math.random() * (max - min + 1)) + min);
};
