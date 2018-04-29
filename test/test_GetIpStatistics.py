captions = ['IP forwarding', 'Default initial TTL', 'Number of received datagrams', 'Number of received datagrams with header errors', 'Number of received datagrams with address errors', 'Number of datagrams forwarded', 'Number of received datagrams with an unknown protocol', 'Number of received datagrams discarded', 'Number of received datagrams delivered', 'Number of outgoing datagrams requested to transmit', 'Number of outgoing datagrams discarded for routing', 'Number of outgoing datagrams discarded', 'Number of outgoing datagrams with no route to destination discarded', 'Fragment reassembly timeout', 'Number of datagrams that required reassembly', 'Number of datagrams successfully reassembled', 'Number of datagrams that could not be reassembled', 'Number of datagrams fragmented successfully', 'Number of datagrams not fragmented and discarded', 'Number of fragments created', 'Number of interfaces', 'Number of IP addresses', 'Number of routes']

from pywingui.windows import *
from pywingui.wtl import *
from pywingui import comctl
from pywingui.lib import form
from pywingui.error import NO_ERROR

from pywingui.network.iphlpapi import GetIpStatistics

comctl.InitCommonControls(comctl.ICC_USEREX_CLASSES)

class Form(form.Form):
	_form_menu_ = [(MF_POPUP, '&File', [(MF_STRING, '&Exit', form.ID_EXIT)])]
	_window_title_ = 'GetIpStatistics Example'

	def __init__(self, *args, **kwargs):
		form.Form.__init__(self, *args, **kwargs)      
		#~ self.list_view.SetItemCount(len(captions))
		#~ self.list_view.SetRedraw(1)
		lvcolumn = comctl.LVCOLUMN(comctl.LVCF_TEXT|comctl.LVCF_WIDTH, 0, 500, 'item')
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
		dwRetval, pStats = GetIpStatistics()
		if dwRetval != NO_ERROR:
			print('GetIpStatistics call failed with %d' % dwRetval)
		else:
			if hasattr(pStats, 'dwForwarding'):
				items[0].pszText = '%d' % pStats.dwForwarding
			else:
				items[0].pszText = '(%d) %d' % (pStats.u.dwOldFieldName, pStats.u.enumNewFieldName)
			items[1].pszText = '%d' % pStats.dwDefaultTTL
			items[2].pszText = '%d' % pStats.dwInReceives
			items[3].pszText = '%d' % pStats.dwInHdrErrors
			items[4].pszText = '%d' % pStats.dwInAddrErrors
			items[5].pszText = '%d' % pStats.dwForwDatagrams
			items[6].pszText = '%d' % pStats.dwInUnknownProtos
			items[7].pszText = '%d' % pStats.dwInDiscards
			items[8].pszText = '%d' % pStats.dwInDelivers
			items[9].pszText = '%d' % pStats.dwOutRequests
			items[10].pszText = '%d' % pStats.dwRoutingDiscards
			items[11].pszText = '%d' % pStats.dwOutDiscards
			items[12].pszText = '%d' % pStats.dwOutNoRoutes
			items[13].pszText = '%d' % pStats.dwReasmTimeout
			items[14].pszText = '%d' % pStats.dwReasmReqds
			items[15].pszText = '%d' % pStats.dwReasmOks
			items[16].pszText = '%d' % pStats.dwReasmFails
			items[17].pszText = '%d' % pStats.dwFragOks
			items[18].pszText = '%d' % pStats.dwFragFails
			items[19].pszText = '%d' % pStats.dwFragCreates
			items[20].pszText = '%d' % pStats.dwNumIf
			items[21].pszText = '%d' % pStats.dwNumAddr
			items[22].pszText = '%d' % pStats.dwNumRoutes
			for item in items:
				self.list_view.SetItem(item)

	def OnCreate(self, event):
		self.list_view = comctl.ListView(parent = self, rcPos = RECT(5, 10, 200, 100, orExStyle = WS_EX_CLIENTEDGE))
		self.controls.Add(form.CTRL_VIEW, self.list_view)
		self.controls.Add(form.CTRL_STATUSBAR, comctl.StatusBar(parent = self))

if __name__ == '__main__':
	mainForm = Form(rcPos = RECT(0, 0, 640, 480))
	mainForm.ShowWindow()

	application = Application()
	application.Run()
