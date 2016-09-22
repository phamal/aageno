#!/bin/sh



function printHelpAndExit {
  echo "Usage: $0 {bidreleased|todaystable|killtheport|auctionss} "
	exit 1;
}

function bidreleased {
    curl "http://dev.bidsync.com:9480/notification-web/rs/event/new/BidReleased/DPXWEBBID/"$1
}

function auctionss {
    curl "http://dev.bidsync.com:9480/notification-web/rs/event/new/LinksBidReleased_For_SuggestedSuppliers/DPXAUCTION/"$1
}

function todaystable {
    curl "http://dev.bidsync.com:9480/notification-web/rs/test/notificationMessagesTableForToday"
}

function killtheport {
   # kill -15 $(`lsof -i :$1 -t` )
   pid=$(lsof -i:$1 -t); kill -TERM $pid || kill -KILL $pid
}



case $1 in
    bidreleased)
      echo  "Bid was released " $2
      bidreleased $2
      echo ""
      ;;
    todaystable)
      todaystable
      echo ""
      ;;
    killtheport)
      killtheport $1
    ;;
    auctionss)
      auctionss $2
    ;;
    *)
      echo "Unknow  command: $1"
      printHelpAndExit
      ;;
esac


