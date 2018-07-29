#filename: shopAPP.py
#encoding = utf - 8
import wx
class RegisterFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, -1, u'register', size = (300, 300))
        
        panel = wx.Panel(self)
        Sizer = wx.BoxSizer( wx.VERTICAL )
        panel.SetSizer(Sizer)
		
        SText1 = wx.StaticText(panel, -1, u'username:')
        Sizer.Add(SText1, 0, wx.TOP|wx.LEFT, 20)
		
        TCtrl1 = wx.TextCtrl(panel, -1)
        Sizer.Add(TCtrl1, 0, wx.TOP|wx.LEFT, 20)
    	
        SText2 = wx.StaticText(panel, -1, u'password:')
        Sizer.Add(SText2, 0, wx.TOP|wx.LEFT, 20)
        	
        TCtrl2 = wx.TextCtrl(panel, -1)
        Sizer.Add(TCtrl2, 0, wx.TOP|wx.LEFT, 20)
		
        btn = wx.Button(panel, -1, u'save')
        Sizer.Add(btn, 0, wx.TOP|wx.LEFT, 20)	

        self.Centre()
class RegisterApp(wx.App):
    def OnInit(self):
        self.frame = RegisterFrame(None)
        self.frame.Show(True)
        return True

class LogInFrame(wx.Frame):
    usersname = {'Admin'
   'administrator']
    def __init__( self, parent):
        wx.Frame.__init__ (self, parent, -1, 'log in', size = (320, 300))
        	
        panel = wx.Panel(self)
        Sizer = wx.BoxSizer( wx.VERTICAL )
        panel.SetSizer(Sizer)
		
        self.SText1 = wx.StaticText(panel, -1, u'username:')
        Sizer.Add(self.SText1, 0, wx.TOP|wx.LEFT, 20)
		
        self.TCtrl1 = wx.TextCtrl(panel, -1)
        Sizer.Add(self.TCtrl1, 0, wx.TOP|wx.LEFT, 20)
       
        self.SText2 = wx.StaticText(panel, -1, u'password:')
        Sizer.Add(self.SText2, 0, wx.TOP|wx.LEFT, 20)
        	
        self.TCtrl2 = wx.TextCtrl(panel, -1)
        Sizer.Add(self.TCtrl2, 0, wx.TOP|wx.LEFT, 20)
		
        self.btn1 = wx.Button(panel, -1, u'log in')
        Sizer.Add(self.btn1, 0, wx.TOP|wx.RIGHT, 20)
        self.Bind(wx.EVT_BUTTON, self.LogIn, self.btn1)
		
        self.btn2 = wx.Button(panel, -1, u'register')
        Sizer.Add(self.btn2, 0, wx.TOP|wx.RIGHT, 20)
        self.Bind(wx.EVT_BUTTON, self.Register, self.btn2)               
        self.a = self.TCtrl1.GetValue()
        self.b = self.TCtrl2.GetValue()
        self.Centre()
    
    def LogIn (self, event):
        if self.a in self.usersname:
            x = self.usersname.index(self.a)
            if self.password[x] == b:
                self.dlg1 =  wx.MessageDialog(None, u"You are the admin.", u"welcome!", wx.CANCEL | wx.ICON_QUESTION)
                self.dlg1.ShowModal()
            else:
                self.dlg2 =  wx.MessageDialog(None, u"there is something wrong.", u"wrong!", wx.CANCEL | wx.ICON_QUESTION)
                self.dlg2.ShowModal()
        else:
            self.dlg3 = wx.MessageDialog(None, u"there is something wrong.", u"wrong!", wx.CANCEL | wx.ICON_QUESTION)
            self.dlg3.ShowModal()
    def Register (self, event):
        app = RegisterApp()
        app.MainLoop()
class LogInApp(wx.App):
    def OnInit(self):
        self.frame = LogInFrame(None)
        self.frame.Show(True)
        return True

    def OnExit(self):
        wx.Exit()

class WelcomeFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, u'welcome', size = (320, 300))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        txt = wx.StaticText(panel, -1, u'Hello! please log in?')
        sizer.Add(txt, 0,wx.TOP|wx.LEFT, 100)
        
        button1 = wx.Button(panel, -1, u'ok')
        sizer.Add(button1, 0, wx.TOP|wx.LEFT, 50)
        self.Bind(wx.EVT_BUTTON, self.LogIn, button1)

        button2 = wx.Button(panel, -1, u'cancel')
        sizer.Add(button2, 0, wx.TOP|wx.LEFT, 50)
        self.Bind(wx.EVT_BUTTON, self.Quit, button2)

        self.Centre()
    def LogIn(self, event):
        self.Close(True)
        app = LogInApp()
        app.MainLoop()
    def Quit(self, event):
        self.Close(True)
class WelcomeApp(wx.App):
    def OnInit(self):
        self.frame = WelcomeFrame(None)
        self.frame.Show(True)
        return True

    def OnExit(self):
        wx.Exit()
app = WelcomeApp()
app.MainLoop()
