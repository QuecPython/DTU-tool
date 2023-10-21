vertical_start_pos = "245"
from translation import tr

class CloudConfig(object):

    # 华为云 界面模板
    def huaweiyun_interface(self, panel):
        huaweiyun_list = [  
                            'wx.StaticText({}, wx.ID_ANY, u"DK", pos=(20, {}+00))'.format(panel, vertical_start_pos),
                            'wx.TextCtrl({}, 805, "", pos=(170, {}+00))'.format(panel, vertical_start_pos),
                            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+00))'.format(
                                panel, tr("NOTE: device name"), vertical_start_pos),

                            'wx.StaticText({}, wx.ID_ANY, u"DS", pos=(20, {}+30))'.format(panel, vertical_start_pos),
                            'wx.TextCtrl({}, 806, "", pos=(170, {}+30))'.format(panel, vertical_start_pos),
                            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+30))'.format(
                                panel, tr("NOTE: device secret key"), vertical_start_pos),
                           
                            'wx.StaticText({}, wx.ID_ANY, "keep_alive", pos=(20, {}+60))'.format(panel, vertical_start_pos),
                            'wx.TextCtrl({}, 807, "", pos=(170, {}+60))'.format(panel, vertical_start_pos),
                            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+60))'.format(
                                panel, tr("NOTE: client request timeout seconds, default{}(s), optional.").format(300), vertical_start_pos),

                            'wx.StaticText({}, wx.ID_ANY, u"clean_session", pos=(20, {}+90))'.format(panel, vertical_start_pos),
                            'wx.ComboBox({}, wx.ID_ANY, pos=(170, {}+90), choices=["0", "1"],style=wx.CB_READONLY)'.format(panel, vertical_start_pos),
                            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+90))'.format(
                                panel, tr("NOTE: clean session, default 0, optional."), vertical_start_pos),

                            'wx.StaticText({}, wx.ID_ANY, u"QOS", pos=(20, {}+120))'.format(panel, vertical_start_pos),
                            'wx.ComboBox({}, wx.ID_ANY, pos=(170, {}+120), choices=["0", "1"],style=wx.CB_READONLY)'.format(panel, vertical_start_pos),
                            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+120))'.format(
                                panel, tr("NOTE: QOS, default 0, optional."), vertical_start_pos),

                            'wx.StaticText({}, wx.ID_ANY, u"subscribe", pos=(20, {}+150))'.format(panel, vertical_start_pos),
                            'wx.TextCtrl({}, 808, "", pos=(170, {}+150), size=wx.Size(320, -1))'.format(panel, vertical_start_pos),
                            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(500, {}+150))'.format(
                                panel, tr("NOTE: multi topic separate by comma."), vertical_start_pos),

                            'wx.StaticText({}, wx.ID_ANY, u"publish", pos=(20, {}+180))'.format(panel, vertical_start_pos),
                            'wx.TextCtrl({}, 809, "", pos=(170, {}+180), size=wx.Size(320, -1))'.format(panel, vertical_start_pos),
                            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(500, {}+180))'.format(
                                panel, tr("NOTE: multi topic separate by comma."), vertical_start_pos)]

        return huaweiyun_list

    def quecthing_interface(self, panel):
        quecthing_list = [
            'wx.StaticText({}, wx.ID_ANY, u"DK", pos=(20, {}+0))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 805, "", pos=(170, {}+0))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+0))'.format(
                panel, tr("NOTE: device name."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, u"PK", pos=(20, {}+30))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 806, "", pos=(170, {}+30))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+30))'.format(
                panel, tr("NOTE: Product Key."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, u"DS", pos=(20, {}+60))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 807, "", pos=(170, {}+60))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+60))'.format(
                panel, tr("NOTE: device secret key."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, u"PS", pos=(20, {}+90))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 808, "", pos=(170, {}+90))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+90))'.format(
                panel, tr("NOTE: Product Key."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, "keep_alive", pos=(20, {}+120))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 809, "", pos=(170, {}+120))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+120))'.format(
                panel, tr("NOTE: client request timeout seconds, default{}(s), optional.").format(120), vertical_start_pos),
            
            'wx.StaticText({}, wx.ID_ANY, u"clean_session", pos=(20, {}+150))'.format(panel, vertical_start_pos),
            'wx.ComboBox({}, wx.ID_ANY, pos=(170, {}+150), choices=[u"关闭", u"开启"],style=wx.CB_READONLY)'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+150))'.format(
                panel, tr("NOTE: clean session, default 0, optional."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, u"QOS", pos=(20, {}+180))'.format(panel, vertical_start_pos),
            'wx.ComboBox({}, wx.ID_ANY, pos=(170, {}+180), choices=["0", "1"],style=wx.CB_READONLY)'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+180))'.format(
                panel, tr("NOTE: QOS, default 0, optional."), vertical_start_pos),
        ]

        return quecthing_list
    
    # socket 界面模板
    def socket_interface(self, panel):
        socket_list = [
                        'wx.StaticText({}, wx.ID_ANY, "IP type", pos=(20, {}+0))'.format(panel, vertical_start_pos),
                        'wx.ComboBox({}, wx.ID_ANY, pos=(170, {}+0), choices=["IPv4", "IPv6"],style=wx.CB_READONLY)'.format(panel, vertical_start_pos),
                        
                        'wx.StaticText({}, wx.ID_ANY, "server", pos=(20, {}+30))'.format(panel, vertical_start_pos),
                        'wx.TextCtrl({}, 803, "", pos=(170, {}+30))'.format(panel, vertical_start_pos),
                        'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+30))'.format(
                            panel, tr("NOTE: port excluded."), vertical_start_pos),

                        'wx.StaticText({}, wx.ID_ANY, "server port", pos=(20, {}+60))'.format(panel, vertical_start_pos),
                        'wx.TextCtrl({}, 804, "", pos=(170, {}+60))'.format(panel, vertical_start_pos),
                        'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+60))'.format(
                            panel, tr("NOTE: port between 1~65536"), vertical_start_pos),

                        'wx.StaticText({}, wx.ID_ANY, "keep_alive", pos=(20, {}+90))'.format(panel, vertical_start_pos),
                        'wx.TextCtrl({}, 806, "", pos=(170, {}+90))'.format(panel, vertical_start_pos),
                        'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+90))'.format(
                            panel, tr("NOTE: set tcp keepalive interval minutes(1~120)."), vertical_start_pos)
        ]

        return socket_list

    # aliyun/txyun 界面模板
    def aliyun_txyun_interface(self, panel):
        aliyun_txyun_list = ['wx.StaticText({}, wx.ID_ANY, "burning_method", pos=(20, {}+0))'.format(panel, vertical_start_pos),
                             'wx.ComboBox({}, wx.ID_ANY, pos=(170, {}+0), choices=["0", "1"],style=wx.CB_READONLY)'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+0))'.format(
                                 panel, tr("NOTE: 0:one key for one product; 1:one key for one device."), vertical_start_pos),

                             'wx.StaticText({}, wx.ID_ANY, "keep_alive", pos=(20, {}+30))'.format(panel, vertical_start_pos),
                             'wx.TextCtrl({}, 804, "", pos=(170, {}+30))'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+30))'.format(
                                 panel, tr("NOTE: client request timeout seconds, default{}(s), optional.").format(300), vertical_start_pos),

                             'wx.StaticText({}, wx.ID_ANY, u"client_id", pos=(20, {}+60))'.format(panel, vertical_start_pos),
                             'wx.TextCtrl({}, 805, "", pos=(170, {}+60))'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+60))'.format(
                                 panel, tr("NOTE: customize client id."), vertical_start_pos),

                             'wx.StaticText({}, wx.ID_ANY, u"DK", pos=(20, {}+90))'.format(panel, vertical_start_pos),
                             'wx.TextCtrl({}, 806, "", pos=(170, {}+90))'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+90))'.format(
                                 panel, tr("NOTE: device name."), vertical_start_pos),

                             'wx.StaticText({}, wx.ID_ANY, u"PK", pos=(20, {}+120))'.format(panel, vertical_start_pos),
                             'wx.TextCtrl({}, 807, "", pos=(170, {}+120))'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+120))'.format(
                                 panel, tr("NOTE: Product Name."), vertical_start_pos),

                             'wx.StaticText({}, wx.ID_ANY, u"DS", pos=(20, {}+150))'.format(panel, vertical_start_pos),
                             'wx.TextCtrl({}, 808, "", pos=(170, {}+150))'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+150))'.format(
                                 panel, tr("NOTE: device secret key."), vertical_start_pos),

                             'wx.StaticText({}, wx.ID_ANY, u"PS", pos=(20, {}+180))'.format(panel, vertical_start_pos),
                             'wx.TextCtrl({}, 809, "", pos=(170, {}+180))'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+180))'.format(
                                 panel, tr("NOTE: Product Key."), vertical_start_pos),

                             'wx.StaticText({}, wx.ID_ANY, u"clean_session", pos=(20, {}+210))'.format(panel, vertical_start_pos),
                             'wx.ComboBox({}, wx.ID_ANY, pos=(170, {}+210), choices=["0", "1"],style=wx.CB_READONLY)'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+210))'.format(
                                 panel, tr("NOTE: clean session, default 0, optional."), vertical_start_pos),

                             'wx.StaticText({}, wx.ID_ANY, u"QOS", pos=(20, {}+240))'.format(panel, vertical_start_pos),
                             'wx.ComboBox({}, wx.ID_ANY, pos=(170, {}+240), choices=["0", "1"],style=wx.CB_READONLY)'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+240))'.format(
                                 panel, tr("NOTE: QOS, default 0, optional."), vertical_start_pos),

                             'wx.StaticText({}, wx.ID_ANY, u"subscribe", pos=(20, {}+270))'.format(panel, vertical_start_pos),
                             'wx.TextCtrl({}, 812, "", pos=(170, {}+270), size=wx.Size(320, -1))'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(500, {}+270))'.format(
                                 panel, tr("NOTE: multi topic separate by comma."), vertical_start_pos),
                             
                             'wx.StaticText({}, wx.ID_ANY, u"publish", pos=(20, {}+300))'.format(panel, vertical_start_pos),
                             'wx.TextCtrl({}, 813, "", pos=(170, {}+300), size=wx.Size(320, -1))'.format(panel, vertical_start_pos),
                             'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(500, {}+300))'.format(
                                 panel, tr("NOTE: multi topic separate by comma."), vertical_start_pos)]

        return aliyun_txyun_list
    
    # mqtt 界面模板
    def mqtt_interface(self, panel):
        mqtt_list = [
            'wx.StaticText({}, wx.ID_ANY, "server", pos=(20, {}+0))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 803, "", pos=(170, {}+0))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+0))'.format(
                panel, tr("NOTE: port excluded."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, "server port", pos=(20, {}+30))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 804, "", pos=(170, {}+30))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+30))'.format(
                panel, tr("NOTE: port between 1~65536."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, "client_id", pos=(20, {}+60))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 805, "", pos=(170, {}+60))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+60))'.format(
                panel, tr("NOTE: customize client id."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, "username", pos=(20, {}+90))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 806, "", pos=(170, {}+90))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+90))'.format(
                panel, tr("NOTE: username registered on server."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, "password", pos=(20, {}+120))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 807, "", pos=(170, {}+120))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+120))'.format(
                panel, tr("NOTE: your password."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, "keep_alive", pos=(20, {}+150))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 808, "", pos=(170, {}+150))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+150))'.format(
                panel, tr("NOTE: client request timeout seconds, default{}(s), optional.").format(30), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, u"clean_session", pos=(20, {}+180))'.format(panel, vertical_start_pos),
            'wx.ComboBox({}, 809, choices=["0", "1"], style=wx.CB_READONLY, pos=(170, {}+180))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+180))'.format(
                panel, tr("NOTE: clean session, default 0, optional."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, u"QOS", pos=(20, {}+210))'.format(panel, vertical_start_pos),
            'wx.ComboBox({}, 810, choices=["0", "1", "2"], style=wx.CB_READONLY, pos=(170, {}+210))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(290, {}+210))'.format(
                panel, tr("NOTE: QOS, default 0, optional."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, u"subscribe", pos=(20, {}+240))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 811, "", pos=(170, {}+240), size=wx.Size(320, -1))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(500, {}+240))'.format(
                panel, tr("NOTE: multi topic separate by comma."), vertical_start_pos),

            'wx.StaticText({}, wx.ID_ANY, u"publish", pos=(20, {}+270))'.format(panel, vertical_start_pos),
            'wx.TextCtrl({}, 811, "", pos=(170, {}+270), size=wx.Size(320, -1))'.format(panel, vertical_start_pos),
            'wx.StaticText({}, wx.ID_ANY, \"{}\", pos=(500, {}+270))'.format(
                panel, tr("NOTE: multi topic separate by comma."), vertical_start_pos)
        ]

        return mqtt_list
