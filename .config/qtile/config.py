from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus right in stack pane"),
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus left in stack pane"),
    Key([mod], "m", lazy.layout.maximize(),
        desc="Maximize"),
    
    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([mod, "control"], "l", lazy.layout.swap_right(),
        desc="Move window right in current stack "),
    Key([mod, "control"], "h", lazy.layout.swap_left(),
        desc="Move window left in current stack "),
    
    Key([mod, "shift"], "j", lazy.layout.grow()),
    Key([mod, "shift"], "k", lazy.layout.shrink()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawn("rofi -show"),
        desc="Rofi"),
    Key([mod], "e", lazy.spawn("google-chrome-stable"),
        desc="google-chrome-stable"),
    Key([mod], "p", lazy.spawn("pulsemixer"),
        desc="pulsemixer"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(margin=7),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(margin=10, name='mo', border_normal='1b2128', border_focus='e25987'),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(margin=7, add_after_last=True),
    layout.VerticalTile(margin=2, name='vt'),
    layout.Max(name='ma'),
    # layout.TreeTab(),
    # layout.Floating(name='fl'),
    # layout.Zoomy(),
]

widget_defaults = dict( font='Ubuntu Bold',
    fontsize=12,
    padding=8,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(padding = 0, scale = 0.6),
                widget.GroupBox(hide_unused=True, block_highlight_text_color='e25987', borderwidth=1, highlight_method='border'),
                # widget.Chord(
                    # chords_colors={
                        # 'launch': ("#ff0000", "#ffffff"),
                    # },
                    # name_transform=lambda name: name.upper(),
                # ),
                widget.WindowName(),
                widget.Systray(),
                widget.Spacer(length=5),
                widget.CPU(format='  {freq_current}GHz {load_percent}%'),
                widget.Memory(),
                widget.Spacer(length=5),
                widget.DF(visible_on_warn=False, format='{uf} {m}'),
                widget.Spacer(length=5),
                widget.Wlan(format='WIFI {percent:2.0%}'),
                widget.PulseVolume(limit_max_volume=True),
                widget.Spacer(length=5),
                widget.Clock(format='%d.%m.%Y %H:%M:%S'),
                widget.QuickExit(),
            ],
            # background='#1b2128'
            24,
            background='#1b2128'
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
