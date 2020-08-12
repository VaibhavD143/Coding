HashMap<Character,Integer> hm = new HashMap<>();
		hm.put('a', 0);
		hm.put('b', 1);
		hm.put('c', 2);
		hm.put('d', 3);
		hm.put('e', 4);
		hm.put('f', 5);
		hm.put('g', 6);
		hm.put('h', 7);
		hm.put('i', 8);
		hm.put('j', 9);
		hm.put('k', 10);
		hm.put('l', 11);
		hm.put('m', 12);
		hm.put('n', 13);		
		hm.put('o', 14);
		hm.put('p', 15);
		hm.put('q', 16);
		hm.put('r', 17);
		hm.put('s', 18);
		hm.put('t', 19);
		hm.put('u', 20);
		hm.put('v', 21);
		hm.put('w', 22);
		hm.put('x', 23);
		hm.put('y', 24);
		hm.put('z', 25);
		
		int a[] = new int[s.length()];
		int i = 0;
		for(i=0;i<s.length();i++)
		{
			int charIndex = hm.get(s.charAt(i));		
			a[i] = Character.getNumericValue(charValue.charAt(charIndex));
		}
		
		int l = 0;
		int r = 0;
		int w = 0;
		int count = 0;
		int li = 0;
		
		for(r=0;r<a.length;r++)
		{
			if(a[r]==0)
				count++;
			
			while(count>k)
			{
				if(a[l]==0)
					count--;
				
				l++;
			}
			
			if(r-l+1>w)
			{
				w = r - l + 1;
				li = l;
			}
		}
		
		return w;