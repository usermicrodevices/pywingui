## 	   Copyright (c) 2003 Henk Punt

## Permission is hereby granted, free of charge, to any person obtaining
## a copy of this software and associated documentation files (the
## "Software"), to deal in the Software without restriction, including
## without limitation the rights to use, copy, modify, merge, publish,
## distribute, sublicense, and/or sell copies of the Software, and to
## permit persons to whom the Software is furnished to do so, subject to
## the following conditions:

## The above copyright notice and this permission notice shall be
## included in all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
## EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
## MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
## NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
## LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
## OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
## WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

from pywingui.windows import *
from pywingui.wtl import *
from pywingui.lib import form


class MyForm(form.Form):
    """sample showing how a form can be prevented from closing by
    overriding the OnClose method of Form"""
    
    _window_icon_ = _window_icon_sm_ = Icon(lpszName = 'blinky.ico')
    _window_title_ = "Test close" 

    _form_menu_ = [(MF_POPUP, "&File",
                    [(MF_STRING, "&New\bCtrl+N", form.ID_NEW),
                     (MF_SEPARATOR,),
                     (MF_STRING, "&Exit", form.ID_EXIT)])]

    _form_accels_ = [(FCONTROL|FVIRTKEY, ord("N"), form.ID_NEW)]

    _form_exit_ = form.EXIT_ONLASTDESTROY

    def OnNew(self, event):
        newForm = MyForm()
        newForm.ShowWindow()

    cmd_handler(form.ID_NEW)(OnNew)

    def OnClose(self, event):
        res = MessageBox(self.handle, "Really close?", "Test Close", MB_YESNO | MB_ICONQUESTION)
        if res == IDYES: event.handled = False #mark as unhandled, default handler will close window


if __name__ == '__main__':
    mainForm = MyForm()        
    mainForm.ShowWindow()

    application = Application()
    application.Run()
