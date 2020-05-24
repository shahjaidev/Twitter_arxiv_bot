var
    twit = require('twit'),
    config = require('./config');
	axios = require('axios');
	cheerio = require('cheerio');
var T = new twit(config);

var tweeted_set = new Set();


function tweet (){

  global.tweet="";
  
  const spawn = require('child_process').spawn;
  const pyProg = spawn('python', ['./js_scrape.py']);

  pyProg.stdout.on('data', (data) => {
  
    console.log(data);
    tweet=data.toString() ;
  });

    if (tweeted_set.has(tweet)==true )
    {
                    const pyProg = spawn('python', ['./js_scrape.py']);

                  pyProg.stdout.on('data', (data) => 
                  {
                    console.log("Repeated, rescraping");
                    console.log(data);
                    tweet=data.toString() ;

                  })
    }
    

T.post('statuses/update', {
        status: tweet

    }, onTweeted);
    //});

    tweeted_set.add(tweet);
  //console.log(tweeted_set)
}

tweet()

//12 hours: 4.32e+7
setInterval(tweet,4.32e+7)


   function onTweeted(err, reply) {
        if (err !== undefined) {
            console.log(err)
        } else {
            console.log('Tweeted: ' + reply.text)
        }
    }
