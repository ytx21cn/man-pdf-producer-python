from enum import Enum


# See man page "console_codes(4)" for the list of colors

class FgColor(Enum):
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    BROWN = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'


class BgColor(Enum):
    BLACK = '40'
    RED = '41'
    GREEN = '42'
    BROWN = '43'
    BLUE = '44'
    MAGENTA = '45'
    CYAN = '46'
    WHITE = '47'


def get_colored_str(content: str, fg_color: FgColor = None, bg_color: BgColor = None):
    color_template = '\033[%sm'
    reset_color_ctrl_seq = color_template % '0'

    has_fg_color = isinstance(fg_color, FgColor)
    has_bg_color = isinstance(bg_color, BgColor)
    content_is_colored = has_fg_color or has_bg_color

    fg_color_ctrl_seq = (color_template % fg_color.value) \
        if has_fg_color else ''
    bg_color_ctrl_seq = (color_template % bg_color.value) \
        if has_bg_color else ''
    end_ctrl_seq = reset_color_ctrl_seq \
        if content_is_colored else ''

    result = '%s%s%s%s' % (fg_color_ctrl_seq, bg_color_ctrl_seq,
                           content, end_ctrl_seq)
    return result
