#!/usr/bin/env python3
from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand       = 'start'
        self.MirrorCommand      = [f'mirror',    f'm']
        self.QbMirrorCommand    = [f'qbmirror',  f'qbm']
        self.YtdlCommand        = [f'ytdl',      f'yt']
        self.LeechCommand       = [f'leech',     f'l']
        self.QbLeechCommand     = [f'qbleech',   f'qbl']
        self.YtdlLeechCommand   = [f'ytdlleech', f'ytl']
        self.CancelAllCommand   = [f'cancelall', 'cancelallbot']
        self.RestartCommand     = [f'restart',   'restartall']
        self.StatusCommand      = [f'status',    'sall']
        self.PingCommand        = [f'ping',      'p']
        self.StatsCommand       = [f'stats',     's']
        self.CloneCommand       = f'clone'
        self.CountCommand       = f'count'
        self.DeleteCommand      = f'del'
        self.CancelMirror       = f'abort'
        self.ListCommand        = f'list'
        self.SearchCommand      = f'search'
        self.UsersCommand       = f'users'
        self.AuthorizeCommand   = f'authorize'
        self.UnAuthorizeCommand = f'unauthorize'
        self.AddSudoCommand     = f'addsudo'
        self.RmSudoCommand      = f'rmsudo'
        self.HelpCommand        = f'help'
        self.LogCommand         = f'log'
        self.ShellCommand       = f'shell'
        self.EvalCommand        = f'eval'
        self.ExecCommand        = f'exec'
        self.ClearLocalsCommand = f'clearlocals'
        self.BotSetCommand      = f'bsetting'
        self.UserSetCommand     = f'usetting'
        self.BtSelectCommand    = f'btsel'
        self.RssCommand         = f'rss'
        self.CategorySelect     = f'catsel'
        self.RmdbCommand        = f'rmdb'
        self.RmalltokensCommand = f'rmat'

BotCommands = _BotCommands()
