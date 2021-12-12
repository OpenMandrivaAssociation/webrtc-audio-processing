%define major 0
%define libprocessing %mklibname webrtc-processing %{major}
%define libcoding %mklibname webrtc-coding %{major}
%define devname %mklibname webrtc -d

Summary:	Real-Time Communication Library for Web Browsers
Name:		webrtc-audio-processing
Version:	1.0
Release:	4
License:	BSD-3-Clause
Group:		System/Libraries
Url:		http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:	https://gitlab.freedesktop.org/pulseaudio/webrtc-audio-processing/-/archive/v%{version}/webrtc-audio-processing-v%{version}.tar.gz
Patch0:		https://gitweb.gentoo.org/repo/gentoo.git/plain/media-libs/webrtc-audio-processing/files/1.0-abseil-cmake.patch
Patch1:		e74894baebe0bba7a7fe37ae0a46a2e9b1b2e021.patch
Patch2:		webrtc-audio-processing-v1.0-add-missing-header.patch
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
%autosetup -n %{name}-v%{version} -p1

%build
%meson -Dcpp_std=gnu++17
%meson_build

%install
%meson_install
