#!/usr/bin/env python3
"""Plan exact constant-frame-rate timing and noninclusive preview sample positions."""
import argparse
from fractions import Fraction
import json
import sys


def frame_plan(fps, *, seconds=None, frames=None, samples=5):
    rate = Fraction(str(fps))
    if rate <= 0:
        raise ValueError('Frame rate must be positive.')
    if (seconds is None) == (frames is None):
        raise ValueError('Provide exactly one of seconds or frames.')
    if seconds is not None:
        duration = Fraction(str(seconds))
        if duration <= 0:
            raise ValueError('Duration must be positive.')
        count = duration * rate
        if count.denominator != 1:
            raise ValueError('Duration does not span whole frames. Choose --frames explicitly.')
        count = count.numerator
    else:
        if isinstance(frames, bool) or not isinstance(frames, int) or frames <= 0:
            raise ValueError('Frame count must be a positive integer.')
        count = frames
        duration = Fraction(count, 1) / rate
    if isinstance(samples, bool) or not isinstance(samples, int) or not 1 <= samples <= count:
        raise ValueError('Sample count must be an integer between 1 and the frame count.')
    indices = [0] if samples == 1 else [i * (count - 1) // (samples - 1) for i in range(samples)]
    return {
        'fps_exact': str(rate),
        'frame_count': count,
        'duration_seconds_exact': str(duration),
        'duration_seconds': float(duration),
        'frame_range': {'start_inclusive': 0, 'end_exclusive': count},
        'samples': [{'frame': i, 'time_seconds_exact': str(Fraction(i, 1) / rate),
                     'time_seconds': float(Fraction(i, 1) / rate)} for i in indices],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fps', required=True, help='Positive number or rational, e.g. 30 or 30000/1001')
    duration = parser.add_mutually_exclusive_group(required=True)
    duration.add_argument('--seconds', help='Exact positive duration; must span whole frames')
    duration.add_argument('--frames', type=int, help='Positive frame count')
    parser.add_argument('--samples', type=int, default=5)
    args = parser.parse_args()
    try:
        result = frame_plan(args.fps, seconds=args.seconds, frames=args.frames, samples=args.samples)
    except (ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
