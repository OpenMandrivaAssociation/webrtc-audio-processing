%define major 1

%define libprocessing %mklibname webrtc-processing
%define libcoding %mklibname webrtc-coding
%define devname %mklibname webrtc -d

%define veryoldlibprocessing %mklibname webrtc-processing 0
%define veryoldlibcoding %mklibname webrtc-coding 0
%define oldlibprocessing %mklibname webrtc-processing 1
%define oldlibcoding %mklibname webrtc-coding 1

Summary:	Real-Time Communication Library for Web Browsers
Name:		webrtc-audio-processing
Version:	1.3
Release:	1
License:	BSD-3-Clause
Group:		System/Libraries
Url:		http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:	https://gitlab.freedesktop.org/pulseaudio/webrtc-audio-processing/-/archive/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	meson
BuildRequires:	abseil-cpp-devel

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

#----------------------------------------------------------------------------

%package -n %{libprocessing}
Summary:	Real-Time Communication Library for Web Browsers
Group:		System/Libraries
%rename		%{oldlibprocessing}
Obsoletes:	%{veryoldlibprocessing} < %{EVRD}

%description -n %{libprocessing}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%files -n %{libprocessing}
%{_libdir}/libwebrtc-audio-processing-1.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libcoding}
Summary:	Real-Time Communication Library for Web Browsers
Group:		System/Libraries
%rename		%{oldlibcoding}
Obsoletes:	%{veryoldlibcoding} < %{EVRD}

%description -n %{libcoding}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%files -n %{libcoding}
%{_libdir}/libwebrtc-audio-coding-1.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Real-Time Communication Library for Web Browsers
Group:		Development/C
Requires:	%{libprocessing} = %{EVRD}
Requires:	%{libcoding} = %{EVRD}
Provides:	webrtc-audio-processing-devel = %{EVRD}
Provides:	webrtc-audio-processing-devel-static = %{EVRD}
Obsoletes:	%{mklibname webrtc -d -s} < 0.1-2

%description -n %{devname}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%files -n %{devname}
%doc AUTHORS COPYING NEWS README
%{_includedir}/webrtc-audio-processing-1/
%{_libdir}/libwebrtc-audio-processing-1.so
%{_libdir}/libwebrtc-audio-coding-1.so
%{_libdir}/pkgconfig/webrtc-*.pc

#----------------------------------------------------------------------------

%prep
%autosetup  -p1

%build
%meson
%meson_build

%install
%meson_install
