#!/usr/bin/env python3

from pathlib import Path
import sys

if __name__ == '__main__':
    core = Path(__file__).parent.parent.joinpath('core')
    sys.path.append(str(core))

    from auth import gen_token
    gen_token()
