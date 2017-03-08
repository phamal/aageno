import {Component, ChangeDetectorRef, Injectable} from '@angular/core';

@Component({
  selector: 'my-app',
  template: `
  <div style="padding: 15px;">
  <div class="form-group" style="width: 700px;">
      <label>Type Something:</label>
      <input [(ngModel)]="typed" placeholder="Type something"  class="form-control">
     
      <br />
      <button type="button" class='btn btn-default' (click)="takeAction()">{{getActionType()}}</button>
      {{assist()}}    
    </div>
  </div>  
`,
})


export class AppComponent  {
  public typed : String;
  public actionType : String;
  public suggestion : String;
  public typedWords : string[];
  public cdr;

  constructor(){
    this.typed = "";
    this.actionType = "Search";
  }


  public takeAction():void{
    console.log("Take appropriation action for "+this.typed);
  }

  public assist():String{
    this.suggestion = "";
    this.typedWords = this.typed.split(" ");
    var wordsCount = this.typedWords.length;

    if(this.typed.search("##") > -1){
      this.suggestion = "Open note of title";
    }else if(wordsCount == 1 && this.typed.search("#") > -1){
      this.suggestion = "Searching something by a tag(#)";
    }else if(wordsCount > 5){
      this.suggestion = "Looks like you are trying to save note";
    }
    return this.suggestion;
  }

  public getActionType():String{
    return this.actionType;
  }



}
