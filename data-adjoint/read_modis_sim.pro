; IDL procedure  -  read_modis_sim.pro
;
;****************************************************************************
;
; NAME:
;      read_modis_sim
;
; PURPOSE:
;      Read a MODIS simulated radiance file produced by shdom2modis
;
;
; CALLING SEQUENCE:
;      read_modis_sim, filename, ierr, ncross, nalong, ndir, mu, phi, 
;                      cross_size, along_size, radpix
;
; INPUTS:
;      filename:  a string with the directory path and file name
;
; OUTPUTS:
;      ierr:       error number (ierr=0 means successful open)
;      ncross:     number of pixels in cross-track direction
;      nalong:     number of pixels in along-track direction
;      ndir:       number of output radiance directions
;      mu:         cosine zenith angle of outgoing radiance [fltarr(ndir)]
;      phi:        azimuth angle of outgoing radiance (deg) [fltarr(ndir)]
;      cross_size: size of MODIS image in cross track direction (km) [fltarr(ndir)]
;      along_size: size of MODIS image in along track direction (km) [fltarr(ndir)]
;      radpix:     radiance array [fltarr(ncross,nalong,ndir)]
;
;
; MODIFICATION HISTORY:
;      Written by:   Frank Evans, July 2009
;
;
;****************************************************************************

PRO read_modis_sim, filename, ierr, ncross, nalong, ndir, mu, phi, $
                    cross_size, along_size, radpix
		
;****************************************************************************

;  Open file and get grid size from the header
openr,lun, filename, /get_lun, error=ierr
if (ierr NE 0) then return
ncross=1 & nalong=1 & ndir=1
readf,lun, ncross, nalong, ndir
ss = ' '
readf,lun, ss
readf,lun, ss

mu = fltarr(ndir)
phi = fltarr(ndir)
cross_size = fltarr(ndir)
along_size = fltarr(ndir)
radpix = fltarr(ncross,nalong,ndir)
buffer = fltarr(ncross+1,nalong)
id=1 & muin=1.0 & theta=0.0 & phiin=0.0 & xsize=8.0 & ysize=8.0

 ; Read in data
for idir = 0, ndir-1 do begin
  readf,lun, id, muin, theta, phiin, xsize, ysize
  if (id-1 NE idir) then begin
    print , 'Incorrect format in ',filename
    stop
  endif
  mu[idir] = muin
  phi[idir] = phiin
  cross_size[idir] = xsize
  along_size[idir] = ysize
  readf,lun, buffer
  radpix[*,*,idir] = buffer[1:ncross,*]
endfor

free_lun, lun

END
