gdb-git-migration
=================

Scripts and files for migrating gdb+binutils to git


Instructions
------------

These are just basic instructions, not including stuff like making new
directories and cd'ing to the right spot for various operations.

* Start with a copy of the old "devo" CVSROOT 

* Grab sourceware's "src" CVSROOT using rsync-command

* Check out the "old gdb releases" git repository

* Convert devo:

  cvs2git --options=options-devo.py
  make-git-repository

* Hack it:

  hack-devo-branch

* Convert src:

  sh -x RemoveFiles
  cvs2git --options=options-src.py
  make-git-repository

* Hack up old-gdb-releases:

  Rewrite-index-old-releases

* Merge:

  run graft-and-filter twice, first old->devo, then devo->src


File details
------------

* RemoveFiles

  A script to remove files from a copy of the "src" tree.

  We mirror src locally, then copy it and remove the bits that don't
  belong in the resulting repository.  Then we run cvs2git on the
  result.

* Rewrite-index-old-releases

  Pedro made a git repository of the old gdb releases:

      https://github.com/palves/gdb-old-releases

  First, based on some archaeology, it seems we want to ignore old
  releases after gdb 3.5 -- anything newer than that is in the "devo"
  copy we have.

  However, the files in these old revisions in this repository appear
  in "./"; but for the conversion we want them to appear in "gdb/".

  This script can be used with filter-branch to rewrite this
  repository:

        git filter-branch --tree-filter Rewrite-index-old-releases -- --all

* Total-merged-user-map

  A list of all the user ids in the repository.

  I started with the gdb and binutils user maps from Jim Meyering's
  cvs->git mirror.  I removed the dups somewhat arbitrarily.

  Then I ran:

        git log --all --format=%aN |sort -u  > ../USERS

  on an early conversion of the "devo" repository to get all the
  older users.  I used merge-authors.py to merge this with the
  Meyering map.

  Next I got logins from the "src" cvs->git conversion and looked
  those up in sourceware's /etc/passwd.

  Finally I asked on the list for updates.

* rsync-command

  rsync the "src" repository
