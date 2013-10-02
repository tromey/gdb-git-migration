gdb-git-migration
=================

Scripts and files for migrating gdb+binutils to git


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

* rsync-command

  rsync the "src" repository

