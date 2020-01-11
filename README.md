# headpats
 A simple pygame script for generating HEADPATS animations, [like so](https://twitter.com/Foone/status/1215479542959075328)

 I've included sample images for [a windows 3.1 icon](https://twitter.com/win_icons/status/1215392811354247168) and [my twitter avatar](https://twitter.com/Foone). 

## Requirements:
* [Python 2.7](https://www.python.org/)
* [pygame](https://www.pygame.org/news) (tested with 1.9.5)

## Customizing

1. Provide your own background image (for example, your twitter avatar), and change BACKGROUND_IMAGE to point to it
2. Optionally, provide a different hand image. This should be at approximately 10x scale, and have a transparent background. Set HAND_IMAGE to this image.
3. Run headpats.py and see how the alignment looks
4. Adjust HORIZONTAL_POSITION if it needs to be farther left (smaller values) or right (bigger values) 
5. Adjust PAT_OFFSET if it needs to be higher up (smaller) or lower (bigger)
6. Adjust PAT_MULT if the hand needs to move farther or less far per pat. Bigger values mean more movement.
7. Adjust TIME_DIV if the hand needs to move slower or faster. Bigger values move slower.

## Capturing

I didn't build in any function to directly create the GIFs, I instead captured the program running using [OBS](https://obsproject.com/).

## License

All code is GPL3. The example images come from iconart.dll and Microsoft Windows 95.