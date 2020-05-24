@app.route('/toptwtr', methods=['GET'])
def toptwtr():
  """ return top papers """
  ttstr = request.args.get('timefilter', 'day') # default is day
  tweets_top = {'day':tweets_top1, 'week':tweets_top7, 'month':tweets_top30}[ttstr]
  cursor = tweets_top.find().sort([('vote', pymongo.DESCENDING)]).limit(100)
  papers, tweets = [], []
  for rec in cursor:
    if rec['pid'] in db:
      papers.append(db[rec['pid']])
      tweet = {k:v for k,v in rec.items() if k != '_id'}
      tweets.append(tweet)
  ctx = default_context(papers, render_format='toptwtr', tweets=tweets,
                        msg='Top papers mentioned on Twitter over last ' + ttstr + ':')
  return render_template('main.html', **ctx)