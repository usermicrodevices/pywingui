captions = ['Host Name', 'Domain Name', 'DNS Servers']

from pywingui.windows import *
from pywingui.wtl import *
from pywingui import comctl
from pywingui.lib import form
from pywingui.error import NO_ERROR

from pywingui.network.iphlpapi import GetNetworkParams

comctl.InitCommonControls(comctl.ICC_USEREX_CLASSES)

class Form(form.Form):
	_form_menu_ = [(MF_POPUP, '&File', [(MF_STRING, '&Exit', form.ID_EXIT)])]
	_window_title_ = 'GetNetworkParams Example'

	def __init__(self, *args, **kwargs):
		form.Form.__init__(self, *args, **kwargs)      
		#~ self.list_view.SetItemCount(len(captions))
		#~ self.list_view.SetRedraw(1)
		lvcolumn = comctl.LVCOLUMN(comctl.LVCF_TEXT|comctl.LVCF_WIDTH, 0, 400, 'item')
		self.list_view.InsertColumn(0, lvcolumn)
		lvcolumn = comctl.LVCOLUMN(comctl.LVCF_TEXT|comctl.LVCF_WIDTH, 0, 100, 'value')
		self.list_view.InsertColumn(1, lvcolumn)
		item_flags = comctl.LVIF_TEXT|comctl.LVIF_DI_SETITEM
		items = []
		for i in range(len(captions)):
			item = comctl.LVITEM(item_flags)
			item.iItem = i
			item.pszText = captions[i]
			self.list_view.InsertItem(item)
			# now setup second column of current row, change iSubItem
			item.iSubItem = 1
			item.pszText = 'value %d' % i
			self.list_view.SetItem(item)
			items.append(item)
		dwRetval, FixedInfo, buf_len = GetNetworkParams()
		if dwRetval != NO_ERROR:
			print('GetNetworkParams failed with error %d' % dwRetval)
		else:
			items[0].pszText = FixedInfo.HostName
			items[1].pszText = FixedInfo.DomainName
			dns_server_list = FixedInfo.DnsServerList.IpAddress.String
			pIPAddr = FixedInfo.DnsServerList.Next
			while pIPAddr:
				dns_server_list += '; ' + pIPAddr[0].IpAddress.String
				pIPAddr = pIPAddr.Next
			items[2].pszText = dns_server_list
			for item in items:
				self.list_view.SetItem(item)

	def OnCreate(self, event):
		self.list_view = comctl.ListView(parent = self, rcPos = RECT(5, 10, 200, 100, orExStyle = WS_EX_CLIENTEDGE))
		self.controls.Add(form.CTRL_VIEW, self.list_view)
		self.controls.Add(form.CTRL_STATUSBAR, comctl.StatusBar(parent = self))

if __name__ == '__main__':
	mainForm = Form(rcPos = RECT(0, 0, 550, 240))
	mainForm.ShowWindow()

	application = Application()
	application.Run()
