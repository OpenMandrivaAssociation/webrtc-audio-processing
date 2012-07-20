%define oname           webrtc
%define major           0
%define libname         %mklibname %{oname} %{major}
%define develname       %mklibname %{oname} -d
%define develname_static       %mklibname %{oname} -d -s

Name:           webrtc-audio-processing
Version:        0.1
Release:        1
Summary:        Real-Time Communication Library for Web Browsers
License:        BSD-3-Clause
Group:          System/Libraries
Source0:	http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/webrtc-audio-processing-%{version}.tar.xz
Url:		http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	libtool
BuildRequires:	make
Patch0:         webrtc-ppc64.patch

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n	%{libname}
Summary:        Real-Time Communication Library for Web Browsers
Group:          System/Libraries

%description -n %{libname}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n	%{develname}
Summary:        Real-Time Communication Library for Web Browsers
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:	webrtc-audio-processing-devel = %{version}-%{release}

%description -n %{develname}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n	%{develname_static}
Summary:        Real-Time Communication Library for Web Browsers
Group:          Development/C
Requires:       %{develname} = %{version}-%{release}
Provides:	webrtc-audio-processing-devel-static = %{version}-%{release}

%description -n %{develname_static}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%prep
%setup -q 
%patch0 -p1

%build
%configure2_5x
%make LIBS="-lpthread"

%install
%makeinstall

%files -n %{libname}
%doc AUTHORS COPYING NEWS PATENTS README
%{_libdir}/libwebrtc_audio_processing.so.%{major}
%{_libdir}/libwebrtc_audio_processing.so.%{major}.*

%files -n %{develname}
%{_includedir}/webrtc_audio_processing
%{_libdir}/libwebrtc_audio_processing.so
%{_libdir}/pkgconfig/webrtc-audio-processing.pc

%files -n %{develname_static}
%{_libdir}/libwebrtc_audio_processing.a
