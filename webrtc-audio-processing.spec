%define oname webrtc
%define major 0
%define libname %mklibname %{oname} %{major}
%define develname %mklibname %{oname} -d

%define _disable_ld_no_undefined 1

Name:		webrtc-audio-processing
Version:	0.1
Release:        3
Summary:	Real-Time Communication Library for Web Browsers
License:	BSD-3-Clause
Group:		System/Libraries
Url:		http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:	http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/webrtc-audio-processing-%{version}.tar.xz
Patch0:		webrtc-ppc64.patch
Patch1:		webrtc-aarch64.patch	

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n %{libname}
Summary:	Real-Time Communication Library for Web Browsers
Group:		System/Libraries

%description -n %{libname}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n %{develname}
Summary:	Real-Time Communication Library for Web Browsers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	webrtc-audio-processing-devel = %{version}-%{release}
Provides:	webrtc-audio-processing-devel-static = %{version}-%{release}
Obsoletes:	%{mklibname webrtc -d -s} < 0.1-2

%description -n %{develname}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
%configure2_5x \
	--disable-static

%make LIBS="-lpthread"

%install
%makeinstall_std
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/libwebrtc_audio_processing.so.%{major}
%{_libdir}/libwebrtc_audio_processing.so.%{major}.*

%files -n %{develname}
%doc AUTHORS COPYING NEWS PATENTS README
%{_includedir}/webrtc_audio_processing
%{_libdir}/libwebrtc_audio_processing.so
%{_libdir}/pkgconfig/webrtc-audio-processing.pc
