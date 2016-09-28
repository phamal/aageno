#!/bin/sh

WILDFLY_BASE="/apps/web"
LOG_BASE="/apps/web/logs"
ADMIN_PORT=""
DEBUG_PORT=""
CODE_PATH=""
ARTIFACT_PATH=""
ARTIFACT_FILE=""
DOMAIN=$1;
ACTION=$2;


function dist {
    cd $CODE_PATH;
    ant dist
}

function start {
    echo "Starting "$DOMAIN;
}

function undeploy {
    echo "Undeploying "$DOMAIN ;
}

function stop {
    echo "Stopping "$DOMAIN;
}

function restart {
    echo "Restarting "$DOMAIN ;
}

function redeploy {
    echo "Redeploying "$DOMAIN;
}

function main {


    case $DOMAIN in
    dpx)
        ADMIN_PORT="9191"
        DEBUG_PORT="9109"
        CODE_PATH="/apps/code/bidsync/dpx"
        ARTIFACT_PATH="/apps/code/bidsync/dpx/target/deploy"
        ARTIFACT_FILE="dpx-war.war"
        ;;
    cas)
        ADMIN_PORT="9291"
        DEBUG_PORT="9209"
        CODE_PATH="/apps/code/bidsync/cas"
        ARTIFACT_FILE="bidsync-cas-war.war"
        ;;
    bidsync)
        ADMIN_PORT="9391"
        DEBUG_PORT="9309"
        CODE_PATH="/apps/code/bidsync"
        ARTIFACT_PATH="/apps/code/bidsync/bidsync-app/target/deploy"
        ARTIFACT_FILE="bidsync-app-ear.ear"
        LOGFILE="$LOG_BASE/wf_refactor.log"
        ;;
    notification)
        ADMIN_PORT="9491"
        DEBUG_PORT="9409"
        CODE_PATH="/apps/code/bidsync/notification"
        ARTIFACT_PATH="/apps/code/bidsync/notification/target/deploy"
        ARTIFACT_FILE="notification-ear.ear"
        ;;
    idp)
        echo "idp is not implemented on wildfly9 yet"
        ADMIN_PORT="9691"
        DEBUG_PORT="9609"
        ;;
    picketlink)
        echo "picketlink is not implemented on wildfly9 yet"
        ADMIN_PORT="9791"
        DEBUG_PORT="9709"
        ;;
    security)
        SECURITY="true"
      	;;
    *)
      	echo "Wildfly application \"$1\" not found!"
        printHelpAndExit
      	;;
  esac

  case $ACTION in
    dist)
        dist
        ;;
    start)
        start
        ;;
    restart)
        restart
        ;;
    stop)
        stop
        ;;
    undeploy)
        undeploy
        ;;
    redeploy)
        redeploy
        ;;
    *)
        echo "Action not found "
        ;;
    esac
}




main