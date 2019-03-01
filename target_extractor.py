def targetExtractor(df,company):
	df['target_'+company]=0
	for i in range(0,len(df)):	
		if company in df['companies'][i]:
			df['target_'+company][i]=1;
		else:
			df['target_'+company][i]=0;
	return df
	
