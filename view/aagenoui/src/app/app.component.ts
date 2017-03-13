import {Component, ChangeDetectorRef, Injectable, OnInit} from '@angular/core';
import {NoteService} from "./services/note.service";
import {Note} from "./model/Note";

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
 providers: [NoteService]
})



export class AppComponent  implements OnInit {
  public typed : String;
  public actionType : String;
  public suggestion : String;
  public typedWords : string[];
  public note : Note;
  public errorMessage : String;


  constructor(private noteService : NoteService){
    this.typed = "";
    this.actionType = "Search";
    this.note = new Note();
  }

  ngOnInit():void{
  }


  public takeAction():void{

    console.log("Take appropriation action for "+this.typed);
    this.getNote("nic");
    console.log(this.note.title)
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

  public getNote(title:String){
    this.noteService.getNote(title)
      .subscribe(
        note => this.note = note,
        error =>  this.errorMessage = <any>error);
  }



}
