def convert_grams(grams):
    ounces = 28.3495231 * grams
    return ounces


grams = int(input())
print(convert_grams(grams))