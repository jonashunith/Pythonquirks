class AddEntry:
	#		
	def query_bundle_(self,arg):
		a,total = 0,[]
		for q in range(len(arg)):
			[total.append(x) for x in arg[a]]
			a+=1
		return total
			
	def apt_selected(self):
		if block_text.get():
			_apt = new_db_sqlite.Queries_query().query_apartment(aptype_text.get())
			apt_merged = self.query_bundle_(_apt)
			if apnum_text.get():
				try:
					if self.is_rm_available(apt_merged):
						tkinter.messagebox.showerror('Entry Manager',\
						' '+aptype_text.get()+' apartment '+apnum_text.get()+' is occupied')
						eb2.focus_set() #send the highlight to the apartment type field
					else:
						self.send_entries()
						
				except IndexError:
					self.send_entries()
		
	def send_entries(self):
		'''This function collects the input data 
		from the tenant and room fields and feeds them into the 
		backend function t_insert and r_insert'''
		
		#kindly write a sanitizer for your entries
		backend.t_insert(t_name_text.get().title(),
			gender_text.get(),
			mob_num_text.get(),
			address_text.get().title(),
			email_text.get(),
			nation_text.get().title(),
			emg_num_text.get(),
			ct_name_text.get().title(),
			chk_in_text.get(),
			chk_out_text.get())
		backend.r_insert(block_text.get(),
			aptype_text.get(),
			apnum_text.get(),
			status_text.get()
			)
		reset_tenant_entries()
		reset_room_entries()
		tkinter.messagebox.showinfo('Entry Manager','your entry was successful')
		
	def reset_entries(self):
		e1.delete(0,END)
		e2.current(0)
		e3.delete(0,END)
		e4.delete(0,END)
		e5.delete(0,END)
		e6.delete(0,END)
		e7.delete(0,END)
		e8.delete(0,END)
		e10.current(0)
		eb1.current(0)
		eb2.current(0)
		eb3.current(0)
		eb4.current(0)
		
	def is_rm_available(self,arg):
		return apnum_text.get() in arg
