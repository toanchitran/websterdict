# websterdict

This repository contains Webster's Unabridged English Dictionary (from the Gutenberg Project, compiled August 22, 2009) in several formats:

This repository contains [*Webster's Unabridged English Dictionary*](https://www.gutenberg.org/ebooks/29765) (from the [Gutenberg Project](https://www.gutenberg.org/), compiled August 22, 2009) in several formats:

| Format | File |
| --- | --- |
| Original dictionary text file |**WebstersEnglishDictionary.txt** |
| JSON file | **dictionary.json** |

## Formatting
#### `dictionary.json`
A single object of all words and definitions:
```json
{
  "anopheles" : "A genus of mosquitoes which are secondary hosts of the malaria parasites, and whose bite is the usual, if not the only, means of infecting human beings with malaria. Several species are found in the United States. They may be distinguished from the ordinary mosquitoes of the genus Culex by the long slender palpi, nearly equaling the beak in length, while those of the female Culex are very short. They also assume different positions when resting, Culex usually holding the body parallel to the surface on which it rests and keeping the head and beak bent at an angle, while Anopheles holds the body at an angle with the surface and the head and beak in line with it. Unless they become themselves infected by previously biting a subject affected with malaria, the insects cannot transmit the disease.",
  "uniclinal" : "See Nonoclinal.",
  "sarong" : "A sort of petticoat worn by both sexes in Java and the Malay Archipelago. Balfour (Cyc. of India)",
```

## Acknowledgments

- Original repository and Julia script provided by [https://github.com/adambom/dictionary](https://github.com/adambom/dictionary)
- Webster's Unabridged English Dictionary provided by [Project Gutenberg](http://www.gutenberg.net/)

## License

The original dictionary text file is covered by The Gutenberg Project's licensing, please see the file headers for more details. The Swift parsing tool and example output files in this repository are free and distributed under the GNU General Public License, Version 2.

